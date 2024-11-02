# 비선점형 스케줄링
# 도착한 순서대로 처리
from Process import *

def FCFS_run(processes):
    print("FCFS Scheduling: ")
    current_time = 0

    # 간트 차트를 위한 리스트
    gantt_chart = []

    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0

    # 1. 프로세스들을 도착 시간 순으로 정렬
    arrival_time_sorted = sorted(processes, key=lambda x:x.arrival_time)

    # 도착 시간 순으로 프로세스 순서 출력
    for arrival_process in arrival_time_sorted:
        print(f"Process {arrival_process.name}이 {arrival_process.arrival_time}초에 도착하였습니다.")

    print()

    # 2. 도착 순으로 순서대로 프로세스들 처리
    for process in arrival_time_sorted:

        # 비선점형
        # 현재 시간을 해당 프로세스의 도착 시간과 비교하여 최댓값으로 업데이트
        current_time = max(current_time, process.arrival_time)

        # 대기 시간 구함
        waiting_time = current_time - process.arrival_time

        # 응답 시간 설정: 처음 실행될 때 한 번만 설정합니다.
        if process.response_time is None:
            process.response_time = current_time - process.arrival_time


        # 현재 실행중인 프로세스 정보 출력
        print(f"Process {process.name}이 {current_time}초에 실행 시작합니다.")

        # 간트 차트에 추가
        gantt_chart.append((process.name, current_time, current_time + process.burst_time))  # 간트 차트에 추가

        # 현재 시간에 해당 프로세스의 작업 시간을 더함
        current_time += process.burst_time

        # 해당 프로세스의 작업이 완료된 시간 출력
        print(f"Process {process.name}이 {current_time}초에 완료되었습니다. 작업 시간 = {process.burst_time}")

        # 반환 시간 구함
        turnaround_time = waiting_time + process.burst_time
        print(f"대기 시간: {waiting_time}, 반환 시간: {turnaround_time}")

        # 통계 데이터 업데이트
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_response_time += process.response_time


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