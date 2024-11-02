# Shortest Job First
# SJF 스케줄링은 작업시간이 짧은 프로세스 먼저 실행
from Process import *

def SJF_run(processes):
    print("SJF Scheduling: ")
    current_time = 0

    # 간트 차트를 위한 리스트
    gantt_chart = []

    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0

    processes.sort(key=lambda x:(x.arrival_time, x.burst_time))
    # 1. 작업 시간을 기준으로 프로세스 정렬
    Job_time_sorted = sorted(processes, key=lambda x:x.burst_time)

    # 2. 작업 시간이 짧은 프로세스 먼저 실행 (비선점형)
    # 가장 먼저 도착한 프로세스 찾아서 먼저 실행
    first_arrived_process = None
    for process in processes:
        if process.arrival_time <= current_time:
            first_arrived_process = process
            break

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

    # 그 다음 프로세스들은 작업 시간이 짧은 순서대로 진행
    for process in Job_time_sorted:
        if process == first_arrived_process:
            continue

        # 비선점형
        current_time = max(current_time, process.arrival_time)

        # 대기 시간 구함
        waiting_time = current_time - process.arrival_time

        print(f"Process {process.name}이 {current_time}초에 실행 시작했습니다.")

        # 간트 차트에 추가
        gantt_chart.append((process.name, current_time, current_time + process.burst_time))  # 간트 차트에 추가

        current_time += process.burst_time

        print(f"Process {process.name}이 {current_time}초에 작업이 완료되었습니다. 작업 시간 = {process.burst_time}")

        # 반환 시간 구함
        turnaround_time = waiting_time + process.burst_time
        print(f"대기 시간: {waiting_time}, 반환 시간: {turnaround_time}")

        # 통계 데이터 업데이트
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_response_time += waiting_time # 비선점형에서 응답 시간(첫 번째 반응이 나온 시점) = 대기 시간

    # 평균 계산
    num_processes = len(processes)
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_response_time = total_response_time / num_processes

    print("\nAverage Waiting Time: ",avg_waiting_time)
    print("Average Response Time: ",avg_response_time)
    print("Average Turnaround Time: ",avg_turnaround_time)

    # 간트 차트 출력
    print_gantt_chart(gantt_chart)
