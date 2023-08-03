# # 1. 폴더 선택
# echo '1. programmers 2. swea'
# read choice

# if [ $choice -eq 1 ]; then
#     site='programmers'
# elif [ $choice -eq 2 ]; then
#     site='swea'
# else
#     echo '1, 2를 입력해주세요'
#     exit 1
# fi

# 폴더이름 입력
echo '폴더 이름을 입력해주세요'
read problem

# 폴더/파일 생성
mkdir -p "$problem"
touch "$problem/sol.py"
touch "$problem/input.txt"

cat << EOF > "$problem/sol.py"
import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    pass
EOF

echo "$problem/sol.py 파일이 생성되었습니다."
echo "$problem/input.txt 파일이 생성되었습니다."
