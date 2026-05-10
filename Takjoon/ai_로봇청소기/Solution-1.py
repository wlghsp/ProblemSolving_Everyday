

from collections import deque
import sys, os
sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

def input(): return sys.stdin.readline().rstrip()

# N: 격자 크기, K: 로봇 청소기의 개수, L: 테스트 횟수
N, K, L = map(int, input().split()) 
