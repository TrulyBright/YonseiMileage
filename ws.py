import asyncio
import json
# from sanic.exceptions import ConnectionClosed
import crawling

async def get_mileage_data(request, ws):
    try:
        data = json.loads(await asyncio.wait_for(ws.recv(), 30))
    except asyncio.TimeoutError as e:
        # ConnectionClosed가 파이썬 3.8 이상부터는 raise되지 않는 버그가 있음.
        # 따라서 30초 기다렸다가 asyncio.TimeoutError를 띄우는 걸로 대체.
        return
    # hakjungbunho = data.get("hakjungbunho")
    # special = data.get("special")
    majored = data.get("majored")
    # majored_secondly = data.get("majored_secondly")
    # applied_courses = data.get("applied_courses")
    # applied_courses = 6 if applied_courses>6 else applied_courses
    # will_graduate = data.get("will_graduate")
    # first_apply = data.get("first_apply")
    # credit_ratio_whole = data.get("credit_ratio_whole")
    # credit_ratio_whole = 1.0 if credit_ratio_whole>1.0 else credit_ratio_whole
    # credit_ratio_last_semester = data.get("credit_ratio_last_semester")
    # credit_ratio_last_semester = 1.0 if credit_ratio_last_semester>1.0 else credit_ratio_last_semester
    grade = data.get("grade")
    # grade = 4 if grade>4 else grade
    metadata, mileage_result = await crawling.get_mileage_data()
    capacity = metadata["capacity"]
    capacity = capacity[grade] or capacity[0]
