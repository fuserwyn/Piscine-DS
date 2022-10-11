import logging
from analytics import Research
from config import parameters, report, payloads

def make_report():
    try:
        logging.basicConfig(filename='analytics.log', level=logging.DEBUG,
                format='%(asctime)s %(message)s')
        file, num_of_steps, webhook = parameters()
        payload = payloads()
        research = Research(file)
        analytics = research.Analytics(research.file_reader())
        observation = analytics.counts()
        frac_check = analytics.fractions(observation)
        forecast_list = analytics.predict_random(num_of_steps)
        forecast = analytics.calc_random(forecast_list)
        result = report(observation, frac_check, num_of_steps, forecast)
        analytics.save_file(result, "report", "txt")
        research.send_slack_message(payload[0], webhook)
    except ValueError:
        print("Exception is raised")
        research.send_slack_message(payload[1], webhook)

if __name__ == '__main__':
    make_report()
