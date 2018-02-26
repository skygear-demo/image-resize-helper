import skygear
# custom logic to be invoked from SDK, e.g.
# skygear.lambda('food:buy', {'food': 'salmon'}) for JS
@skygear.op('food:buy', user_required=False)
def buy_food(food):
    # TODO: call API about online shopping
    # return an object to the SDK
    return {
        'success': True,
        'food': food,
    }
