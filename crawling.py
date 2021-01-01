import asyncio
import httpx
from lxml import html

URL = "http://ysweb.yonsei.ac.kr:8888/curri120601/curri_pop_mileage_result01.jsp"

async def get_mileage_data(hakjungbunho="CSI2103")->tuple:
    async with httpx.AsyncClient() as client:
        data = {
            "yshs_domain": "H1",
            "yshs_hyhg": "20201",
            "yshs_hakno": hakjungbunho,
            "yshs_bb": "01",
            "yshs_sbb": "00",
        }
        response = await client.post(URL, data=data)
        tree = html.fromstring(response.text)
        capacity = []
        capacity.append(int(tree.xpath("//table[2]/tr[4]/td[7]")[0].text_content())) # 정원
        reserved_for_majoring = int(tree.xpath("//table[2]/tr[4]/td[9]")[0].text_content().split()[0]) # 전공자 정원
        reserved_for_majoring_second = tree.xpath("//table[2]/tr[4]/td[9]")[0].text_content().split()[1][1]=="Y" # 복수전공자 전공자 정원 포함 여부
        capacity.append(int(tree.xpath("//table[2]/tr[4]/td[10]")[0].text_content()))
        capacity.append(int(tree.xpath("//table[2]/tr[4]/td[11]")[0].text_content()))
        capacity.append(int(tree.xpath("//table[2]/tr[4]/td[12]")[0].text_content()))
        capacity.append(int(tree.xpath("//table[2]/tr[4]/td[13]")[0].text_content()))
        open_for_exchange = tree.xpath("//table[2]/tr[4]/td[14]")[0].text_content()=="O"
        max_mileage = int(tree.xpath("//table[2]/tr[4]/td[15]")[0].text_content())
        metadata = {
            "capacity": capacity,
            "reserved_for_majoring": reserved_for_majoring,
            "reserved_for_majoring_second": reserved_for_majoring_second,
            "open_for_exchange": open_for_exchange,
            "max_mileage": max_mileage,
        }
        rows = tree.xpath("//table[3]/tr")[2:] # 결과 목록
        result = []
        for row in rows:
            mileage = int(row.xpath(".//td[2]")[0].text_content()) # 투자 마알리지
            in_reserved = row.xpath(".//td[3]")[0].text_content().split()[1][1]=="Y" # 전공자 정원 포함 여부
            applied_courses = int(row.xpath(".//td[4]")[0].text_content()) # 신청 과목 수
            will_graduate = row.xpath(".//td[5]")[0].text_content()=="Y" # 졸업신청 여부
            first_apply = row.xpath(".//td[6]")[0].text_content()=="Y" # 초수강 여부
            credit_ratio_whole = float(row.xpath(".//td[7]")[0].text_content()) # 총이수학점/졸업이수학점
            credit_ratio_last_semester = float(row.xpath(".//td[8]")[0].text_content()) # 직전학기이수학점/학기당수강학점
            grade = int(row.xpath(".//td[9]")[0].text_content()) # 학년
            succeeded = row.xpath(".//td[10]")[0].text_content()=="O" # 수강여부
            special = row.xpath(".//td[11]")[0].text_content()=="*" # 비고(특수교육대상자)
            result.append({
                "mileage": mileage,
                "in_reserved": in_reserved,
                "applied_courses": applied_courses,
                "will_graduate": will_graduate,
                "first_apply": first_apply,
                "credit_ratio_whole": credit_ratio_whole,
                "credit_ratio_last_semester": credit_ratio_last_semester,
                "grade": grade,
                "succeeded": succeeded,
                "special": special,
            })
        return metadata, result


# response = requests.post(URL, data=data)
# print(response.text)
