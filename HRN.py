# Highest Response Ratio Next
# 대기 시간과 CPU 사용시간 고려
# 대기 시간 + CPU 사용시간 / CPU 사용시간
# 비선점형
from Process import *

def HRN_run(processes):
    print("HRN Scheduling: ")
    current_time = 0

    # 간트 차트를 위한 리스트
    gantt_chart = []

    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0

    num_processes = len(processes)

    # 1. 최고 응답률 우선 순위 순으로 프로세스 정렬
    # 가장 먼저 도착한 프로세스 찾음
    first_arrived_process = None
    for process in processes:
        if process.arrival_time <= current_time:
            first_arrived_process = process
            break

    #SJF와 동일하게 작업시간 짧은 순으로 배열 만듦
    Job_time_sorted = sorted(processes, key=lambda x:x.burst_time)

    # 2. 정렬 된 순서대로 프로세스 처리
    # 2-1. 가장 먼저 도착한 프로세스 먼저 처리
    if first_arrived_process:
        current_time = first_arrived_process.arrival_time

        # 대기 시간 구함
        waiting_time = current_time - first_arrived_process.arrival_time

        print(f"Process {first_arrived_process.name}이 {current_time}초에 실행 시작했습니다.")

        # 간트 차트에 추가
        gantt_chart.append((process.name, current_time, current_time + process.burst_time))  # 간트 차트에 추가

        current_time += process.burst_time

        print(f"Process {first_arrived_process.name}이 {current_time}초에 작업이 완료되었습니다. 작업 시간 = {first_arrived_process.burst_time}")

        # 반환 시간 구함
        turnaround_time = waiting_time + process.burst_time
        print(f"대기 시간: {waiting_time}, 반환 시간: {turnaround_time}")

        # 통계 데이터 업데이트
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_response_time += waiting_time # 비선점형에서 응답 시간(첫 번째 반응이 나온 시점) = 대기 시간

        Job_time_sorted.remove(first_arrived_process)  # 처리된 프로세스는 리스트에서 제거


    while Job_time_sorted:
        hrn_sorted = [] # hrn 우선 순위대로 프로세스들 저장할 리스트

        for process in Job_time_sorted:
            # 프로세스 별 대기 시간 구함 / 프로세스 별 우선 순위 구함 - 함수로 빼서 구현
            response_ratio, wait_time = calculate_response_ratio(process, current_time)
            hrn_sorted.append((process, response_ratio, wait_time))

        # 우선 순위에 따라 프로세스들 정렬
        hrn_sorted.sort(key=lambda x:x[1], reverse=True)

        # hrn_sorted 리스트에서 첫 번째 순서 진행
        next_process = hrn_sorted[0][0]

        # 대기 시간 구함
        waiting_time = current_time - process.arrival_time

        print(f"Process {next_process.name}이 {current_time}초에 실행 시작했습니다. "
              f"현재 시간 = {current_time}, 대기 시간 = {hrn_sorted[0][2]}, HRN 우선순위 = {hrn_sorted[0][1]}")

        # 간트 차트에 추가
        gantt_chart.append((next_process.name, current_time, current_time + next_process.burst_time))  # 간트 차트에 추가

        current_time += next_process.burst_time

        print(f"Process {next_process.name}이 {current_time}초에 작업이 완료되었습니다.")

        # 반환 시간 구함
        turnaround_time = hrn_sorted[0][2] + next_process.burst_time
        print(f"대기 시간: {hrn_sorted[0][2]}, 반환 시간: {turnaround_time}")

        # 통계 데이터 업데이트
        total_waiting_time += hrn_sorted[0][2]
        total_turnaround_time += turnaround_time
        total_response_time += hrn_sorted[0][2] # 비선점형에서 응답 시간(첫 번째 반응이 나온 시점) = 대기 시간

        Job_time_sorted.remove(next_process)  # 처리된 프로세스는 리스트에서 제거

    # 평균 계산
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_response_time = total_response_time / num_processes

    print("\nAverage Waiting Time: ",avg_waiting_time)
    print("Average Response Time: ",avg_response_time)
    print("Average Turnaround Time: ",avg_turnaround_time)

    # 간트 차트 출력
    print_gantt_chart(gantt_chart)


# 프로세스 별 대기 시간, 우선 순위 구하는 함수
def calculate_response_ratio(process, current_time):
    # 프로세스 별 대기 시간 구함
    wait_time = current_time - process.arrival_time

    # 프로세스 별 우선 순위 구함
    response_ratio = (wait_time + process.burst_time) / process.burst_time

    #print(f"Process {process.name}의 우선순위 {response_ratio}")

    return response_ratio, wait_time

