from xml.etree import cElementTree as ET

samplexml = """
<TwilioResponse>
	<SMSMessages page="0" pagesize="50" uri="/2010-04-01/Accounts/AC0e49761a756a6fb79e8ad941c4a0061b/SMS/Messages" firstpageuri="/2010-04-01/Accounts/AC0e49761a756a6fb79e8ad941c4a0061b/SMS/Messages?Page=0&amp;PageSize=50" previouspageuri="" nextpageuri="/2010-04-01/Accounts/AC0e49761a756a6fb79e8ad941c4a0061b/SMS/Messages?Page=1&amp;PageSize=50">
		<SMSMessage>
			<Sid>SM800f449d0399ed014aae2bcc0cc2f2ec</Sid>
			<DateCreated>Mon, 16 Aug 2010 03:45:01 +0000</DateCreated>
			<DateUpdated>Mon, 16 Aug 2010 03:45:03 +0000</DateUpdated>
			<DateSent>Mon, 16 Aug 2010 03:45:03 +0000</DateSent>
			<AccountSid>AC0e49761a756a6fb79e8ad941c4a0061b</AccountSid>
			<To>+14159978453</To>
			<From>+14158141829</From>
			<Body>Hey Jenny why aren't you returning my calls?</Body>
			<Status>sent</Status>
			<Direction>outbound-api</Direction>
			<Price>-0.02000</Price>
			<ApiVersion>2008-08-01</ApiVersion>
			<Uri>/2010-04-01/Accounts/AC0e49761a756a6fb79e8ad941c4a0061b/SMS/Messages/SM800f449d0399ed014aae2bcc0cc2f2ec</Uri>
		</SMSMessage>
        <SMSMessage>
			<Sid>SM800f449d0399ed014aae2bcc0cc2f2ec</Sid>
			<DateCreated>Mon, 17 Aug 2010 03:45:01 +0000</DateCreated>
			<DateUpdated>Mon, 16 Aug 2010 03:45:03 +0000</DateUpdated>
			<DateSent>Mon, 16 Aug 2010 03:45:03 +0000</DateSent>
			<AccountSid>AC0e49761a756a6fb79e8ad941c4a0061b</AccountSid>
			<To>+14159978453</To>
			<From>+14158141829</From>
			<Body>Hey Jenny why aren't you returning my calls?</Body>
			<Status>sent</Status>
			<Direction>outbound-api</Direction>
			<Price>-0.02000</Price>
			<ApiVersion>2008-08-01</ApiVersion>
			<Uri>/2010-04-01/Accounts/AC0e49761a756a6fb79e8ad941c4a0061b/SMS/Messages/SM800f449d0399ed014aae2bcc0cc2f2ec</Uri>
		</SMSMessage>
		...
	</SMSMessages>
</TwilioResponse>
"""

def xml_to_info(xmltext):
    root = ET.fromstring(xmltext)
    msgs = root[0]
    retlist = []
    for msg in list(msgs):
        date = msg.find('DateCreated').text
        sender = msg.find('From').text
        body = msg.find('Body').text
        retlist.append(
            {
                'DateCreated':date,
                'From':sender,
                'Body':body
            }
        )
    return retlist

#print xml_to_info(samplexml)
