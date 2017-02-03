from testing.api_testing.utils import BaseTest
import types
import uuid
import datetime


class CompaniesTests(BaseTest):

    def setUp(self):
        super(CompaniesTests, self).setUp()
        self.response = self.client.api.GetCompanyList()
        self.assertEqual(self.response.status_code, 200)
        self.company = self.response.json()[0]
        self.lg('GetCompanyList [%s] response [%s]' % (self.user, self.response.json()))

    #Currently fail due to issue https://github.com/itsyouonline/identityserver/issues/218
    def test001_post_company(self):
        """ ITSYOU-029
        *Test case for check register a new company POST /companies.*

        **Test Scenario:**

        #. check register a new company, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        global_id = str(uuid.uuid4()).replace('-', '')[0:10]
        public_keys = self.applicationid
        data = {'globalid': global_id, 'publicKeys': public_keys}
        response = self.client.api.CreateCompany(data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(type(response.json()), types.ListType)
        self.lg('%s ENDED' % self._testID)

    #Currently fail due to issue https://github.com/itsyouonline/identityserver/issues/218
    def test002_put_company(self):
        """ ITSYOU-030
        *Test case for check update company PUT /companies/{globalId}.*

        **Test Scenario:**

        #. check update company, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        info = str(uuid.uuid4()).replace('-', '')[0:10]
        date_time = datetime.datetime.now()
        data = {'info': info, 'expire': date_time}
        response = self.client.api.UpdateCompany(data=data, globalId=self.company['globalId'])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(type(response.json()), types.ListType)
        self.lg('%s ENDED' % self._testID)

    #Currently fail due to issue https://github.com/itsyouonline/identityserver/issues/218
    def test003_post_contract(self):
        """ ITSYOU-031
        *Test case for check add new company contract POST /companies/{globalId}/contracts.*

        **Test Scenario:**

        #. check add new company contract, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        response = self.client.api.GetUserOrganizations(self.user)
        organization_id = response.json()['owner'][0]
        response = self.client.api.GetOrganizationContracts(organization_id)
        contractId = response.json()[0]
        content = str(uuid.uuid4()).replace('-', '')[0:10]
        contract_type = str(uuid.uuid4()).replace('-', '')[0:10]
        date_time = datetime.datetime.now()
        data = {'content': content, 'expires': date_time, 'contractId': contractId,
                'contractType': contract_type, 'parties': [], 'signatures': []}
        response = self.client.api.CreateCompanyContract(data=data, globalId=self.company['globalId'])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(type(response.json()), types.ListType)
        self.lg('%s ENDED' % self._testID)