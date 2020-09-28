import threading


def start_threads(base_list, thread_range, target_func) -> None:
    """並列処理"""
    i = 0
    for _ in range(base_list):
        threads = []
        for _ in range(thread_range):
            # index = i*5 + j # 配列の要素のindex
            t = threading.Thread(target=target_func)
            t.setDaemon(True)
            t.start()
            threads.append(t)
        wait_all_threads(threads)
        i += 1


def wait_all_threads(threads) -> None:
    """それぞれのスレッドが終了するまで待つ"""
    for thread in threads:
        thread.join()
    print('スレッド単位が終了')
    return
