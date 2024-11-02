# 선점형 우선순위 스케줄링
# 라운드 로빈 방식 사용
from collections import  deque
from Process import *

def priority_preemptive_run(processes, time_slice=2):
    print("선점형 우선순위 Scheduling: ")
    current_time = 0

    ready_queue = deque()

    # 간트 차트를 위한 리스트
    gantt_chart = []

    # 프로세스들을 도착 시간 순으로 정렬
    processes.sort(key=lambda x: x.arrival_time)

    process_index = 0 # 현재 처리할 프로세스의 인덱스 번호
    completed_processes = 0 # 완료된 프로세스의 수
    n = len(processes) # 전체 프로세스의 수

    total_waiting_time = 0 # 총 대기 시간
    total_turnaround_time = 0 # 총 반환 시간
    total_response_time = 0 # 총 응답 시간

    # 1. 모든 프로세스가 완료될 때까지
    while completed_processes < n:
        # 현재 시간에 도착한 프로세스를 준비 큐에 추가
        while process_index < n and processes[process_index].arrival_time <= current_time:
            proc = processes[process_index]
            ready_queue.append(proc)
            print(f"Process {proc.name}가 준비 큐에 {current_time}초에 삽입되었습니다.")
            process_index += 1

        # 2. 준비 큐에 프로세스가 존재하면 하나 선택 후 실행
        if ready_queue:

            # 정렬 코드 - 선점형 우선순위 : 우선순위 순으로 정렬
            ready_queue = deque(sorted(list(ready_queue), key=lambda x: x.priority))

            process = ready_queue.popleft()
            print(f"Process {process.name}이 {current_time}초에 실행 시작합니다.")

            # 응답 시간 설정: 처음 실행될 때 한 번만 설정
            if process.response_time is None:
                process.response_time = current_time
                print(f"Process {process.name} response time set to {process.response_time} at time {current_time}")

            # 3. 시간 최신화
            # 실행 시간을 타임 슬라이스와 현재 프로세스의 남은 작업 시간 중 작은 값으로 설정
            execute_time = min(time_slice, process.remaining_time)
            # 간트 차트에 추가
            gantt_chart.append((process.name, current_time, current_time + execute_time))  # 간트 차트에 추가

            process.remaining_time -= execute_time # 남은 작업 시간 실행 시간을 이용하여 최신화
            current_time += execute_time # 현재 시간도 최신화

            # 새로운 프로세스가 도착한 경우 준비 큐에 추가
            while process_index < n and processes[process_index].arrival_time <= current_time:
                proc = processes[process_index]
                ready_queue.append(proc)
                print(f"Process {proc.name}가 준비 큐에 {proc.arrival_time}초에 삽입되었습니다.")
                process_index += 1

            # 4-1. 작업을 다 완료하지 못 한 경우 - 다시 준비 큐로
            if process.remaining_time > 0:
                ready_queue.append(process)
                print(f"Process {process.name}가 {process.remaining_time}초 남아서 준비 큐에 {current_time}초에 다시 삽입되었습니다.")

            # 4-2. 작업을 완료한 경우
            else:
                # 프로세스의 시간 최신화
                process.completion_time = current_time # 완료 시간 = 현재 시간
                process.turnaround_time = current_time - process.arrival_time # 반환 시간 = 현재 시간 - 도착한 시간
                process.waiting_time = process.turnaround_time - process.burst_time # 대기 시간 = 반환 시간 - 작업 시간
                completed_processes += 1
                print(f"Process {process.name}이 {current_time}초에 완료되었습니다.")

                # 총 평균 시간 최신화
                total_waiting_time += process.waiting_time
                total_turnaround_time += process.turnaround_time
                total_response_time += process.response_time
        # 준비 큐에 프로세스가 존재 x
        else:
            # 아직 준비 큐에 도착하지 않은 프로세스가 존재하는 경우
            if process_index < n:
                current_time = processes[process_index].arrival_time
            else:
                break

    # 평균 계산
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    avg_response_time = total_response_time / n

    print()
    # 결과 출력
    for proc in processes:
        print(f"Process {proc.name} - 응답 시간: {proc.response_time}, 대기 시간: {proc.waiting_time}, 반환 시간: {proc.turnaround_time}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Response Time: {avg_response_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

    # 간트 차트 출력
    print_gantt_chart(gantt_chart)
