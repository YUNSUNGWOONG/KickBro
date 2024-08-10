import subprocess

"""
터미널에서 "mjpg프로그램을 구동하는" 명령어를 실행하는 예제코드
"""

def run_mjpg_streamer():
    command = 'mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -w /usr/local/share/mjpg-streamer/www/"'
    
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    
    if process.returncode == 0:
        print("Command executed successfully.")
        print(stdout.decode())
    else:
        print("Error executing command.")
        print(stderr.decode())

if __name__ == "__main__":
    run_mjpg_streamer()
