from kavenegar import * 

def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('7768697352574A4F56676A7342327A4650685748345050503331442B4D616B566C4D4576766B507A667A303D') 
        params = {
            'sender' : '',
            'receptor': phone_number, 
            'message': f'{code} کد تایید شما '
        } 
        response = api.sms_send(params) 
        print(response)
    except APIException as e: 
            print(e)
    except HTTPException as e: 
            print(e)
            