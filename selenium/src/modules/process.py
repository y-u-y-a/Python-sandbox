import threading, math

def start_threads(base_list, thread_range, target_func) -> None:
    """並列処理"""
    i = 0
    # 対象の配列の総数 ÷ 立てるスレッド数
    loop_times = math.ceil(len(base_list)/thread_range)
    for _ in range(loop_times):
        threads = []
        for _ in range(thread_range):
            # serial_index = i*thread_range + j # base_listにおけるindex
            t = threading.Thread(target=target_func)
            t.setDaemon(True)
            t.start()
            threads.append(t)
        wait_all_threads(threads)
        i += 1
        return


def wait_all_threads(threads) -> None:
    """それぞれのスレッドが終了するまで待つ"""
    for thread in threads:
        thread.join()
    print('全てのスレッドが終了')
    return