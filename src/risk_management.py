class RiskManagement:
    def __init__(self, position_size: float, stop_loss: float, take_profit: float):
        self.position_size = position_size
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.trailing_stop = None

    def check_stop_loss(self, current_price: float) -> bool:
        return current_price <= self.stop_loss

    def check_take_profit(self, current_price: float) -> bool:
        return current_price >= self.take_profit

    def update_trailing_stop(self, current_price: float, trailing_offset: float):
        if self.trailing_stop is None or current_price > self.trailing_stop:
            self.trailing_stop = current_price - trailing_offset

    def check_trailing_stop(self, current_price: float) -> bool:
        return current_price <= self.trailing_stop