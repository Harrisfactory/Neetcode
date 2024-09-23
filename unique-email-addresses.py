class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        cleanedEmails = set()

        #first seperate domains and store them in an array
        for i in range(len(emails)):
            emails[i] = emails[i].split('@')

        self.cleanPlus(emails)
        self.cleanPeriods(emails)

        for email in emails:
            cleanedEmails.add(email[0]+'@'+email[1])
        return len(cleanedEmails)

    def cleanPlus(self, emails):
        for i in range(len(emails)):
            for j in range(len(emails[i][0])):
                if emails[i][0][j] == '+':
                    emails[i][0] = emails[i][0][:j]
                    break
        
    def cleanPeriods(self, emails):
        for i in range(len(emails)):
            emails[i][0] = emails[i][0].replace('.','')
