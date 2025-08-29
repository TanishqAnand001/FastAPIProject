from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="Tanishq Anand 22BCE0508 OA",
)


class RequestData(BaseModel):
    data: List[str] = Field(..., example=["a", "1", "334", "4", "R", "$"])


class ResponseData(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum_of_numbers: str
    concatenated_reversed_alphabets: str


@app.post("/bfhl", response_model=ResponseData)
async def process_data(request: RequestData):
    try:
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        all_alphabets_str = ""

        for item in request.data:
            if item.replace('.', '', 1).isdigit() or (item.startswith('-') and item[1:].replace('.', '', 1).isdigit()):
                num = int(float(item))
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(num))
                else:
                    odd_numbers.append(str(num))
            elif item.isalpha():
                alphabets.append(item.upper())
                all_alphabets_str += item
            else:
                special_characters.append(item)

        reversed_alphabets = all_alphabets_str[::-1]
        alternating_caps_str = "".join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(reversed_alphabets)])

        response = {
            "is_success": True,
            "user_id": "tanishq_anand_22052004",
            "email": "tanishq.anand2022@vitstudent.ac.in",
            "roll_number": "22BCE0508",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum_of_numbers": str(total_sum),
            "concatenated_reversed_alphabets": alternating_caps_str
        }

        return response
    except Exception:
        return {
            "is_success": False,
            "user_id": "tanishq_anand_22052004",
            "email": "tanishq.anand2022@vitstudent.ac.in",
            "roll_number": "22BCE0508",
            "odd_numbers": [],
            "even_numbers": [],
            "alphabets": [],
            "special_characters": [],
            "sum_of_numbers": "",
            "concatenated_reversed_alphabets": ""
        }


@app.get("/")
async def root():
    return {"message": "API is running. Use the /bfhl endpoint to post data."}
