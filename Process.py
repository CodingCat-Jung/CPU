# data.txt에서 데이터를 읽어온다
# 프로세스 도착시간 작업시간 우선순위

class Process:
    # 생성자 함수
    # 객체를 생성할때 자동으로 호출되며, 클래스의 인스턴스를 초기화
    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name # 프로세스 이름
        self.arrival_time = arrival_time # 도착 시간
        self.burst_time = burst_time # 작업 시간
        self.remaining_time = burst_time # 남은 작업 시간
        self.priority = priority # 우선순위

        self.waiting_time = 0 # 대기 시간을 0으로 초기화
        self.response_time = None # 응답 시간을 None으로 초기화
        self.turnaround_time = 0 # 반환 시간을 0으로 초기화

        self.completion_time = 0 # 완료 시간을 0으로 초기화


# 파일에서 데이터를 읽어오는 함수
def read_process_data(file_name):
    # 프로세스 정보 저장할 리스트 생성
    processes = []

    with open(file_name, 'r') as file:
        for line in file:
            # 한 줄씩 데이터를 읽어와서 공백을 기준으로 나눈다
            data = line.strip().split()

            # 각각의 값을 정수로 변환하여 / Process 객체를 생성하고 리스트에 추가함
            name, arrival_time, burst_time, priority = map(int, data)
            processes.append(Process(name, arrival_time, burst_time, priority))

    return processes

# 간트 차트를 콘솔 창에 출력 시키는 함수
def print_gantt_chart(gantt_chart):
    print("\n간트 차트:")
    # 프로세스 이름 출력 - 윗줄
    for entry in gantt_chart:
        process_name, start_time, end_time = entry # 엔트리에서 프로세스 이름, 시작 시간, 종료 시간을 가져옴
        print(f"| {process_name} ", end="") # 프로세스 이름 출력
    print("|")

    # 시간 출력 - 아랫줄
    time_marker = 0
    print("0", end="")  # 시작 시간 0 출력
    for entry in gantt_chart:
        _, start_time, end_time = entry # 엔트리에서 시작 시간과 종료 시간을 가져온다.(프로세스 이름은 사용하지 않음)
        time_marker = end_time
        print(f"\t{time_marker}", end="") # 종료 시간 출력

    print()  # 줄 바꿈