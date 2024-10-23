
class Ingredient:
    """Ингредиент."""

    def __init__(self, name, raw_weight, weight, cost) -> None:
        self._name = name 
        self._raw_weight = raw_weight 
        self._weight = weight 
        self._cost = cost 

    @property
    def name(self):
        return self._name
    @property
    def raw_weight(self):
        return self._raw_weight
    @property
    def weight(self):
        return self._weight
    @property
    def cost(self):
        return self._cost
    

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Название должно являться строкой")
        self._name = value

    @raw_weight.setter
    def raw_weight(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Чистый вес должен быть указан в числовом значении")
        self._raw_weight = value
    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Вес должен быть указан в числовом значении")
        self._weight = value
    @cost.setter
    def cost(self, value):
        if not isinstance(value, int):
            raise ValueError("Стоимость должна быть типом int")
        self._cost = value



class Receipt:


    def __init__(self,id:int, name:str, ingredient_list_api) -> None:
        self.id = id
        self.name = name
        self.ingredient_list_api = ingredient_list_api
        self.ingredient_list = []

        self._create_ingridiends()


    def _create_ingridiends(self):
        self.ingredient_list = []
        for i in self.ingredient_list_api:
            self.ingredient_list.append(Ingredient(i[0], i[1], i[2], i[3]))



    def calc_cost(self, portions=1):
        cost = 0
        for i in self.ingredient_list:
            cost+=i.cost
        return cost*portions

    def calc_weight(self, portions=1, raw=True):
        weight = 0
        if raw:
            for i in self.ingredient_list:
                weight+=i.raw_weight
            return weight*portions
        else:
            for i in self.ingredient_list:
                weight+=i.weight
            return weight*portions

    def __str__(self) -> str:
        res = f"Рецепт блюда {self.name} (одна порция):"
        for i in self.ingredient_list:
            a = f" - Ингридиент: {i.name}, чистый вес: {i.raw_weight}, вес: {i.weight}, стоимость {i.cost}"




def get_recipe_by_id(recipe_id, recipe_list):
    return next(filter(lambda x: x.id == recipe_id, recipe_list), None)
