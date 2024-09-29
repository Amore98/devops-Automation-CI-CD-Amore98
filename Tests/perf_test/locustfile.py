from locust import HttpUser, task ,between,tag
import json
import random
class CalculatorUser(HttpUser):

    wait_time = between(2, 4)

    def on_start(self):
        pass

    @task(2)
    @tag('add')
    def add(self):
        data = [[1,1,2], [2,2,4] , [-3,3,0]]
        data_to_use = random.choice(data)
        add = {
            "operation": "add",
            "operand1": data_to_use[0],
            "operand2": data_to_use[1]

        }
        with self.client.post("/calculate", catch_response=True, name='add', json=add) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] ==  data_to_use[2]:
                response.failure(f"Expected result to be 2 but was {response_data['result']}")

    @task(1)
    @tag('subtract')
    def subtract(self):
        subtract = {
            "operation": "subtract",
            "operand1": 1,
            "operand2": 1
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=subtract) as response:
            response_data = json.loads(response.text)
            if not response_data['result'] == 0:
                response.failure(f"Expected result to be 0 but was {response_data['result']}")

    @task(1)
    @tag('multiply')
    def multiply(self):
        multiply = {
            "operation": "multiply",
            "operand1": 2,
            "operand2": 3
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=multiply) as response:
            response_data = json.loads(response.text)
            if response_data.get('result') != 6:
                response.failure(f"Expected result to be 6 but was {response_data['result']}")


    @task(1)
    @tag('divide')
    def divide(self):
        divide = {
            "operation": "divide",
            "operand1": 10,
            "operand2": 2
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=divide) as response:
            response_data = json.loads(response.text)
            if response_data.get('result') != 5:
                response.failure(f"Expected result to be 5 but was {response_data['result']}")


if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5001"
    run_single_user(CalculatorUser)


#for the add it takes 6 ms and the other 3 takes  7 ms in 95%

#2222 
### add 6,82 
### subtract 3,27 ms
### multiply 3,4 ms
### suptract 3.27 ms
### total 16,67 ms

## 3333
#740 and the response time is more
