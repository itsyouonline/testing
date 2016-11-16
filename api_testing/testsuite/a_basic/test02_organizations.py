from testing.api_testing.utils import BaseTest
import types
import uuid


class OrganizationsTests(BaseTest):


    def setUp(self):
        super(OrganizationsTests, self).setUp()
        response = self.client.api.GetUserOrganizations(self.user)
        self.lg('GetUserOrganizations [%s] response [%s]' % (self.user, response.json()))
        self.assertEqual(response.status_code, 200)
        self.globalid = response.json()['owner'][0]
        self.lg('organization globalid %s' % self.globalid)

    def test001_post_put_delete_organization(self):
        """ ITSYOU-
        *Test case for check get organization GET /organizations/{globalid}.*

        **Test Scenario:**

        #. check get organizations, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        username = self.user
        globalid = str(uuid.uuid4()).replace('-', '')[0:10]
        data = {'globalid': globalid,
                'dns': [globalid + '.com'],
                'includes': '',
                'owners': [username],
                'members': [],
                'publicKeys': []}
        self.client.api.CreateNewOrganization(data)
        response = self.client.api.GetUserOrganizations(self.user)
        self.lg('GetUserOrganizations [%s] response [%s]' % (username, response.json()))
        self.assertEqual(response.status_code, 200)
        self.client.api.AddOrganizationMember(data, globalid)
        self.client.api.AddOrganizationOwner(data, globalid)
        self.client.api.RemovePendingOrganizationInvitation(username, globalid)
        self.client.api.LeaveOrganization(globalid, username)
        self.client.api.UpdateOrganization(data, globalid)
        self.client.api.DeleteOrganization(globalid)
        response = self.client.api.GetOrganization(self.organization_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)

    def test002_post_put_delete_organization(self):
        """ ITSYOU-
        *Test case for check get organization GET /organizations/{globalid}.*

        **Test Scenario:**

        #. check get organizations, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        username = self.user
        globalid = str(uuid.uuid4()).replace('-', '')[0:10]
        data = {'globalid': globalid,
                'dns': [globalid + '.com'],
                'includes': '',
                'owners': [self.user],
                'members': [],
                'publicKeys': []}
        self.client.api.CreateOrganizationDNS(data, dnsname, globalid)
        self.client.api.UpdateOrganizationDNS(data, dnsname, globalid)
        self.client.api.DeleteOrganizaitonDNS(dnsname, globalid)
        response = self.client.api.GetOrganization(self.organization_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)

    def test003_post_put_delete_organization(self):
        """ ITSYOU-
        *Test case for check get organization GET /organizations/{globalid}.*

        **Test Scenario:**

        #. check get organizations, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        username = self.user
        globalid = str(uuid.uuid4()).replace('-', '')[0:10]
        data = {'globalid': globalid,
                'dns': [globalid + '.com'],
                'includes': '',
                'owners': [self.user],
                'members': [],
                'publicKeys': []}
        self.client.api.CreateNewOrganizationAPIKey(data, globalid)
        self.client.api.GetOrganizationAPIKey(data, globalid)
        self.client.api.GetOrganizationAPIKeyLabels(globalid)
        self.client.api.UpdateOrganizationAPIKey(data, label, globalid)
        self.client.api.DeleteOrganizationAPIKey(label, globalid)
        response = self.client.api.GetOrganization(self.organization_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)

    def test004_post_put_delete_organization(self):
        """ ITSYOU-
        *Test case for check get organization GET /organizations/{globalid}.*

        **Test Scenario:**

        #. check get organizations, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        username = self.user
        globalid = str(uuid.uuid4()).replace('-', '')[0:10]
        data = {'globalid': globalid,
                'dns': [globalid + '.com'],
                'includes': '',
                'owners': [self.user],
                'members': [],
                'publicKeys': []}
        self.client.api.CreateNewSubOrganization(data, globalid)
        self.client.api.AddOrganizationRegistryEntry(data, globalid)
        self.client.api.AddUserRegistryEntry(data, globalid)
        self.client.api.UpdateOrganizationMemberShip(data, globalid)
        self.client.api.DeleteOrganizationRegistryEntry(key, globalid)
        response = self.client.api.GetOrganization(self.organization_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)

    def test005_post_put_delete_organization(self):
        """ ITSYOU-
        *Test case for check get organization GET /organizations/{globalid}.*

        **Test Scenario:**

        #. check get organizations, should succeed
        #. validate all expected keys in the returned response
        """
        self.lg('%s STARTED' % self._testID)
        username = self.user
        globalid = str(uuid.uuid4()).replace('-', '')[0:10]
        data = {'globalid': globalid,
                'dns': [globalid + '.com'],
                'includes': '',
                'owners': [self.user],
                'members': [],
                'publicKeys': []}
        self.client.api.CreateOrganizationContracty(data, globalid)
        self.client.api.GetOrganizationContracts(globalid)
        response = self.client.api.GetOrganization(self.organization_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json()), types.DictType)
        self.lg('%s ENDED' % self._testID)
