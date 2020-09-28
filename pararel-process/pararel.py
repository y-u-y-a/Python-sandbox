import threading


def exec_thred(num_divided_list, thread_range, target_func) -> None:
    """並列処理"""
    i = 0
    for _ in range(num_divided_list):
        threads = []
        for j in range(thread_range):
            # index = i*5 + j
            t = threading.Thread(target=target_func) # thread取得
            t.setDaemon(True)
            t.start()
            threads.append(t)
        # 全てのスレッドを待機
        wait_all_threads(threads)
        i += 1

def wait_all_threads(threads) -> None:
    """それぞれのスレッドが終了するまで待つ"""
    for thread in threads:
        thread.join()
    return
