class Node:
    """Клас для вузла зв’язного списку"""
    def __init__(self, data):
        self.data = data  # Значення вузла
        self.next = None  # Вказівник на наступний вузол

class LinkedList:
    """Клас для однозв’язного списку"""
    def __init__(self):
        self.head = None  # Початково список порожній

    def append(self, data):
        """Додає новий вузол у кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # Якщо список порожній, то новий вузол стає головою
            return
        
        last = self.head
        while last.next:
            last = last.next  # Переміщаємось до останнього вузла
        last.next = new_node  # Додаємо новий вузол у кінець списку

    def display(self):
        """Виводить список у консоль"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Позначаємо кінець списку

    def delete(self, key):
        """Видаляє вузол зі списку за значенням"""
        current = self.head

        # Якщо потрібно видалити перший вузол
        if current and current.data == key:
            self.head = current.next
            del current
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return  # Якщо елемент не знайдено

        prev.next = current.next  # Видаляємо вузол
        del current

# Використання
ll = LinkedList()
l1 = LinkedList()
ll.append(1)
l1.append(2)
ll.append(l1)

print("Початковий список:")
ll.display()

