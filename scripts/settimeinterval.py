def settimeinterval():
    intervals = {
        "1H": 60,
        "2H": 120,
        "3H": 180,
        "4H": 240,
        "5H": 300,
        "6H": 360,
        "7H": 420,
        "8H": 480,
        "9H": 540,
        "10H": 600,
        "11H": 660,
        "12H": 720,
        "13H": 780,
        "14H": 840,
        "15H": 900,
        "16H": 960,
        "17H": 1020,
        "18H": 1080,
        "19H": 1140,
        "20H": 1200,
        "21H": 1260,
        "22H": 1320,
        "23H": 1380,
        "24H": 1440,
        "1D": 1440,
        "2D": 2880,
        "3D": 4320,
        "4D": 5760,
        "5D": 7200,
        "6D": 8640,
        "7D": 10080,
        "8D": 11520,
        "9D": 12960,
        "10D": 14400,
        "11D": 15840,
        "12D": 17280,
        "13D": 18720,
        "14D": 20160,
        "15D": 21600,
        "16D": 23040,
        "17D": 24480,
        "18D": 25920,
        "19D": 27360,
        "20D": 28800,
        "21D": 30240,
        "22D": 31680,
        "23D": 33120,
        "24D": 34560,
        "25D": 36000,
        "26D": 37440,
        "27D": 38880,
        "28D": 40320,
        "29D": 41760,
        "30D": 43200,
    }
    user_resp = input(
        "Define backtesting interval: 1H-24H for hours, 1D-30D for days. \n Your answer: "
    )
    try:
        interval = intervals[user_resp]
    except KeyError:
        user_resp = input(
            "Please re-enter your chouse exactly as 1H for 1 hour, 5D for 5 days and so on and hit return again \n Your answer: "
        )
        interval = intervals[user_resp]
    print(
        "Backtesting interval is set to",
        user_resp,
        "which is exactly ",
        interval,
        "minutes",
    )
    return interval
