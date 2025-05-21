class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    patient1 = Patient("Alice", "10:00 AM")
    patient2 = Patient("Bob", "10:30 AM")

    q.enqueue(patient1)
    q.enqueue(patient2)

    print(f"Next Patient: {q.peek().name}")
    q.dequeue()
    print(f"Next Patient: {q.peek().name}")
