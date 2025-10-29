# Customer order 
- order placed by customer(it has FO and it can have 1 - n FOs)
		if an CO has 2 entities which are in different warehouses then 2 FOs are created
# Fulfilment order 
- order which is sent to warehouse.Fulfillment orders break down customer orders into actionable work units for warehouses, stores, or third-party logistics providers. They contain detailed instructions about what needs to be picked, packed, and shipped from specific locations.

# Release order 
- it is released to warehouse. RO can have more then 1 FO
# Backorder 
- is an order for goods that are currently out of stock but expected to be available and shipped later.Backorders allow retailers to continue accepting orders even when inventory is temporarily unavailable, maintaining sales continuity and capturing demand that would otherwise be lost to competitors

# Order flow:
- When a customer order is created in any channel the connector will publish order to kafka topic and nifi will consume and transform it to nebula order payload and call create order api of order-orchestrator, this will internally trigger camunda workflow. Workflow will call order service's create customer order and save it to db

# Camunda:
- the flow is called process definitions it will have id. Everytime workflow is triggered an instance is created. 

- there are 2 tasks: service task and user task.
  * service task - executes automatically
  * user task - waits for user to approve or review

- gateway is for decision making.

- In service task set implementation as delegate expression and in delegate expression add ${class name (fisrstletter small)}.
The class should implement JavaDelegate interface and it has one method execute where custom logic can be written
- Process definition key is the id of that workflow
- Businesskey is used to uniquely identify instances(ex: ordernumber)
- Field injection: we can set variables in field injection, when service task is triggered it adds that variable to execution variable

- User task:- A spring boot api is exposed and user will call that api, then that api should run the user task by fetching it by id

- Subprocess:
In Collection we have to mention on which subprocesses needs to be created. and in element variable define name for variable where each object will be stored





# Best practices :
- Entity is used to store in db it should be converted to dto to be sent outside, Modelmapper can be used for convert entity to dto



