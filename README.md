# Akamai Purge By URL

Akamai Purge By URL script is intended to simplify purging multiple URLs at once in Akamai Staging or the Production environment, instead of having to do it one at a time through the Akamai Control Center UI.


#Sample output for purging 3 URLs at a time

<code> {"httpStatus":201,"detail":"Request accepted","supportId":"edus-SDZZcJTG25s6Ggc3eN2Ezi","purgeId":"edus-SDZZcJTG25s6Ggc3eN2Ezi","estimatedSeconds":5}

{"httpStatus":201,"detail":"Request accepted","supportId":"edus-SKdAbXTBRb75JPjyYUBg9Z","purgeId":"edus-SKdAbXTBRb75JPjyYUBg9Z","estimatedSeconds":5}

{"httpStatus":201,"detail":"Request accepted","supportId":"edus-SNhQHNbz8VeiAX8fU9he5n","purgeId":"edus-SNhQHNbz8VeiAX8fU9he5n","estimatedSeconds":5}

{'objects': <URLs sent in the POST payload>} <\code>
