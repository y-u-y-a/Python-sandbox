import logging
import time
import math
from pararel import exec_thred, wait_all_threads


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s')


def func() -> None:
    """スレッドごとに実行したい処理"""
    logging.debug(f'start')
    time.sleep(5)
    logging.debug(f'end')



if __name__ == '__main__':

    target_list = ['AAAAA', 'BBBBBB', 'CCCCCCC', 'DDDDDDD', 'EEEEEEEE', 'FFFFFFFF', 'GGGGGGGGG', 'HHHHHHHH', 'IIIIIIIIIII', 'JJJJJJJ']
    # 「会社リスト/5」の整数部分だけ繰り返し
    num_divided_list = math.ceil(len(target_list)/5)
    # 同時に立てるスレッドの数
    thread_range = 5
    # 並列処理()
    exec_thred(num_divided_list=num_divided_list, thread_range=thread_range, target_func=func)
