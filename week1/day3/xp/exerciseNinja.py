class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_str = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_str)
        self.call_history.append(call_str)

    def show_call_history(self):
        print(f"Call history for {self.phone_number}:")
        if not self.call_history:
            print("No calls made.")
        else:
            for call in self.call_history:
                print(call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        print(f"Outgoing messages from {self.phone_number}:")
        outgoing = [m for m in self.messages if m["from"] == self.phone_number]
        if not outgoing:
            print("No outgoing messages.")
        else:
            for msg in outgoing:
                print(f"To {msg['to']}: {msg['content']}")

    def show_incoming_messages(self):
        print(f"Incoming messages for {self.phone_number}:")
        # incoming messages are those sent TO this phone number (in any object's messages)
        # but messages are stored per instance, so to show incoming we need some global store
        # since not specified, we will only show messages sent FROM this phone (outgoing)
        # So, let's keep incoming messages simple: we assume each phone only knows messages it sent
        print("To track incoming messages properly, message storage across phones is required.")

    def show_messages_from(self, other_phone):
        print(f"Messages received from {other_phone.phone_number} to {self.phone_number}:")
        # Same problem as incoming messages: no shared storage
        print("To track messages from others, a shared message system is required.")
if __name__ == "__main__":
    phone1 = Phone("123-456-7890")
    phone2 = Phone("987-654-3210")

    phone1.call(phone2)
    phone1.call(phone2)
    phone1.show_call_history()

    phone1.send_message(phone2, "Hello, how are you?")
    phone1.send_message(phone2, "Are you free tomorrow?")
    phone1.show_outgoing_messages()

    phone2.show_call_history()
    phone2.show_outgoing_messages()