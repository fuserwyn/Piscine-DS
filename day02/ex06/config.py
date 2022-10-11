import logging

# remark - better keep webhook in .env file for security
def parameters():
    file = "data.csv"
    num_of_steps = 3
    webhook = "https://hooks.slack.com/services/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"
    logging.debug("Input parameters are accepted")
    return file, num_of_steps, webhook

def report(observation, frac_check, num_of_steps, forecast):
    res = "Report\n"
    res += "We have made %d observations from tossing a coin: " \
        % (observation[0] + observation[1])
    res += "%d of them were tails and %d of them were heads. " \
        % (observation[0], observation[1])
    res += "The probabilities are %0.2f%% and %0.2f%%, respectively. " \
        % (frac_check[0], frac_check[1])
    res += "Our forecast is that in the next %d observations " % num_of_steps
    res += "we will have: %d tail and %d heads." \
        % (forecast[0], forecast[1])
    logging.debug("Report is created")
    return res

def payloads():
    payload_success = {"text" : "The report has been successfully created"}
    payload_failure = {"text" : "The report hasn’t been created due to an error"}
    logging.debug("Payloads are accepted")
    return payload_success, payload_failure