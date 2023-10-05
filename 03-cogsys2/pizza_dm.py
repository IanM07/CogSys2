# import python_actr module library for Python ACT-R classes
import python_actr
from python_actr.actr import *
from python_actr.actr.hdm import *

class PizzaBuilder_DM(ACTR):
        goal = Buffer()
        retrieval = Buffer()
        DM_module = HDM(retrieval, finst_size=22, finst_time=100.0)
        my_pizza = []
        
        def cook_pizza(self, pizza_ingred):
                '''
                Takes in list of "ingrediants" and outputs a "pizza"
                Inputs: pizza_ingred [list of strings]
                Output: cooked_pizza [string]
                '''
                #Whats going on here? - https://docs.python.org/3/library/stdtypes.html#str.join
                return ("_".join(pizza_ingred))
                
        def init():
                #Add memory chunks to declarative memory module
                #(More chunks needed in DM!)
                DM_module.add("prev:crust next:bbq")
                DM_module.add("prev:bbq next:cheddar")
                DM_module.add("prev:cheddar next:bacon")
                DM_module.add("prev:bacon next:onion")
                
                DM_module.add("prev:crust next:marinara")
                DM_module.add("prev:marinara next:mozzarella")
                DM_module.add("prev:mozzarella next:pepperoni")
                DM_module.add("prev:pepperoni next:onion")
                goal.set("start_pizza")
                
        def prep_ingredients(goal="start_pizza"):
                #start building our pizza!
                goal.set("build_pizza")
                #Request next step from DM
                my_pizza.append("crust")
                DM_module.request("prev:crust next:?next_ingredient")

        ###Rules to request from declarative memory for next step/ingredient and place that ingredient on your pizza and make sure you can move on to cooking pizza

        #If the previous ingredient was crust, the agent will randomly choose between bbq or marinara, add it to the pizza list and query the DM for the next ingredient
        def marinara(goal="build_pizza", retrieval="prev:crust next:?next_ingredient"):
                goal.set("cheese")
                my_pizza.append(next_ingredient)
                DM_module.request("prev:marinara next:?ingredient")

        def bbq(goal="build_pizza", retrieval="prev:crust next:?next_ingredient"):
                goal.set("cheese")
                my_pizza.append(next_ingredient)
                DM_module.request("prev:bbq next:?ingredient")
                
        #If the previous ingredient was marinara or bbq, the agent will choose mozzarella or cheddar respectively, add it to the pizza list and query the DM for the next ingredient
        def mozzarella(goal="cheese", retrieval="prev:marinara next:?next_ingredient"):
                goal.set("meat")
                my_pizza.append(next_ingredient)
                DM_module.request("prev:mozzarella next:?ingredient")
                
        def cheddar(goal="cheese", retrieval="prev:bbq next:?next_ingredient"):
                goal.set("meat")
                my_pizza.append(next_ingredient)
                DM_module.request("prev:cheddar next:?ingredient")
        
        #If the previous ingredient was mozzarella or cheddar, the agent will choose pepperoni or bacon respectively, add it to the pizza list and query the DM for the next ingredient
        def pepperoni(goal="meat", retrieval="prev:mozzarella next:?next_ingredient"):
                goal.set("cook_pizza")
                my_pizza.append(next_ingredient)
                DM_module.request("prev:pepperoni next:onion")

        def bacon(goal="meat", retrieval="prev:?cheddar next:?next_ingredient"):
                goal.set("cook_pizza")
                my_pizza.append(next_ingredient)
                DM_module.request("prev:bacon next:onion")
        
        #This is the final step, and because all pizzas have onions we just add onion here
        def cook_pizza_step(goal="cook_pizza"):
                my_pizza.append("onion")
                my_pizza = self.cook_pizza(my_pizza)
                print("Mmmmmm my " + my_pizza + " pizza is gooooood!")
                self.stop()


class EmptyEnvironment(python_actr.Model):
        pass

env_name = EmptyEnvironment()
agent_name = PizzaBuilder_DM()
env_name.agent = agent_name
python_actr.log_everything(env_name)
env_name.run()

