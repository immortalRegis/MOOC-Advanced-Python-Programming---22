# Write your solution here:
def sort_by_seasons(items: list):
    
    def order_by_seasons(record: dict):
        return record['seasons']

    new_list = items.copy()
    new_list.sort(key=order_by_seasons)
    return new_list

