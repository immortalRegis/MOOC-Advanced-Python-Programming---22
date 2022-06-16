# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def order_by_ratings(item: dict):
        return item['rating']
    
    new_list = items.copy()
    new_list.sort(key=order_by_ratings, reverse=True)
    return new_list