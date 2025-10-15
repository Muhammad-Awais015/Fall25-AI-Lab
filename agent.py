class Model_Based_ReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.memory = {}

    def act(self, room, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"

        if room in self.memory:
            if self.memory[room] == action:
                action = f"Keep {action}"

        self.memory[room] = action
        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desired_temperature = 22
agent = Model_Based_ReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(room, temperature)
    print(f"{room}: Current temperature = {temperature}°C -> {action}")

print(agent.memory)               