# 1. (Process.py)
#    프로세스 함수 호출 - 데이터 읽기
#    라인 읽어서 프로세스 개수 확인 후
#    각 프로세스 별 도착 시간, 작업 시간, 우선순위 읽어와 저장
#
# 2. 각 스케줄링.py 파일
#    Process.py에서 저장한 데이터를 가지고 각각의 스케줄링 코드 실행 - run()
#
# 3. Main.py
#    각각의 내부 함수 run()호출로 각 스케줄링 작업 처리 - (타임 슬라이스=2)

from Process import *
from FCFS import *
from SJF import *
from HRN import *
from RR import *
from SRT import *
from Priority_non_preemptive import *
from Priority_preemptive import *

# 메인 함수 실행 시
# Process에서 read_process_data 함수 불러서 data.txt 파일에서 내용 읽어옴
# processes 리스트에 내용 저장
if __name__ == "__main__":
    file_name = 'data.txt'
    processes = read_process_data(file_name)

    #FCFS_run(processes)
    #SJF_run(processes)
    #HRN_run(processes)
    #RR_run(processes, 2)
    SRT_run(processes, 2)
    #priority_non_preemptive_run(processes)
    #priority_preemptive_run(processes, 2)

