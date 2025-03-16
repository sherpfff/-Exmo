# Основной файл для запуска бота
from src.data_collector import DataCollector
from src.strategy import TradingStrategy
from src.risk_management import RiskManagement

async def main():
    # Инициализация компонентов
    collector = DataCollector(ws_url="wss://api.example.com/websocket", pair="BTC_USD")
    strategy = TradingStrategy(capital=1000, risk_per_trade=0.01)
    risk_manager = RiskManagement(position_size=10, stop_loss=30000, take_profit=40000)

    # Запуск сбора данных
    asyncio.create_task(collector.connect())

    while True:
        data = collector.get_latest_data()
        if data:
            current_price = float(data['last'])
            if strategy.should_buy(current_price):
                print("Сигнал на покупку!")
            elif strategy.should_sell(current_price):
                print("Сигнал на продажу!")

            # Проверка рисков
            if risk_manager.check_stop_loss(current_price):
                print("Стоп-лосс достигнут!")
            if risk_manager.check_take_profit(current_price):
                print("Тейк-профит достигнут!")

        await asyncio.sleep(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())