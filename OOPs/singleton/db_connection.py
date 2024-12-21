import threading
import time
from random import randint

class DbConnection:
    _db_instance = None
    _from_factory = False
    _lock = threading.Lock()  # mutex 

    def __init__(self, connection_name:str, url:str): 
        if not DbConnection._from_factory:
            raise TypeError("You Can not create instance directly")

        self.connection_name = connection_name
        self.url = url
        print(f"[INIT] Created DbConnection instance for : {self.connection_name}, {self.url}")

    @classmethod
    def get_DbConnection(cls, connection_name, url):
        # Ensuring there won't be lock for the repetative access after 
        # once instance of dbConnection is created 
        if not cls._db_instance: # First check (without locking)
            with cls._lock: 
                time.sleep(0.2)
                print(f"[LOCK ACQUIRED] Initializing DbConnection instance for : {connection_name}")
                if not cls._db_instance: # Second check (after locking)
                    # Critical section
                    cls._from_factory = True 
                    cls._db_instance = DbConnection(connection_name, url)
                    cls._from_factory = False
                else: 
                    print(f"[ALREADY INITIALIZED] Returning existing DbConnection instance")

        else: 
            print(f"[ALREADY INITIALIZED] Returning existing DbConnection instance")
                    
        
        return cls._db_instance


# Test function to be run in mltiple threads 
def test_singleton(thread_id, connection_name, url):
    print(f"Thread {thread_id} attempting to get DbConnection instance...")
    instance = DbConnection.get_DbConnection(connection_name, url) 
    print(f"Thread {thread_id} obtained instance: {instance}")


# Main function to simulate multi-threaded environment
def main():
    threads = []
    connection_name = "MainDB"
    url = "https://database.url"

    # Create multiple threads to test the Singleton
    for i in range(10):
        thread = threading.Thread(target=test_singleton, args=(i, connection_name, url))
        threads.append(thread)
        time.sleep(randint(1, 3) / 10)  # Simulate a slight delay between thread starts
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads completed.")

if __name__ == "__main__":
    main()


# def main(): 
#     db_connection = DbConnection.get_DbConnection("External Connection", "url1")
#     db_connection = DbConnection.get_DbConnection("Internal connection", "url2")
#     print(db_connection.connection_name)
#     print(db_connection.url)
