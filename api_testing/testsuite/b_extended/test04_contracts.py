from testing.api_testing.utils import BaseTest
import types
import datetime
import uuid


class ContractsTests(BaseTest):

    def setUp(self):
        super(ContractsTests, self).setUp()
        response = self.client.api.GetUserOrganizations(self.user)
        self.lg('GetUserOrganizations [%s] response [%s]' % (self.user, response.json()))
        self.assertEqual(response.status_code, 200)
        organization_id = response.json()['owner'][0]
        response = self.client.api.GetOrganizationContracts(organization_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.ListType)
        self.contractId = response.json()[0]
        self.lg('contractId %s' % self.contractId)

    #Currently fail due to issue https://github.com/itsyouonline/identityserver/issues/233
    def test001_post_contract_signatures(self):
        """ ITSYOU-032
        *Test case for check add a contract signature POST /contracts/{contractId}/signatures.*

        **Test Scenario:**

        #. check get a contract, should succeed
        #. validate all expected keys in the returned response
        #. post new signature, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        date_time = datetime.datetime.now()
        public_key = self.applicationid
        signature = str(uuid.uuid4()).replace('-', '')[0:10]
        signed_by = str(uuid.uuid4()).replace('-', '')[0:10]
        data = {u'date': date_time, u'publicKey': public_key, u'signature': signature,
                u'signedBy': signed_by}
        response = self.client.api.SignContract(data=data, contractId=self.contractId)
        self.assertEqual(response.status_code, 201)
        response = self.client.api.GetContract(self.contractId)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)