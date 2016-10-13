##Test Case 1: Adding new organization

**Purpose: Test cobranding is working as expected**

**Steps:**

### Show an organization logo on the login/register screen

When you use the authorization code flow to authenticate your users using Itsyou.Online, you can provide a better user experience by showing your logo on the login page.

To set an organization logo go to the settings page of an organization:

![Organization Settings](OrganizationSettingsTab.png)

and add a logo to your organization:

![Set organization logo](SetOrganizationLogo.png)

When a user is asked to login, this logo is added to the login/register page:

![Branded login page](BrandedLoginPage.png)

##Test Case 2: URL redirection integration with another website

**Purpose: Test URL redirection integration with another website is working as expected**

**Steps:**

1. go to website integrated with itsyouonline
2. click the link to sign-in using itsyou.online
3. login using your itsyou.online account and validate that successfully redirect you to the website page with your login information
4. check that you got the required info from your itsyou.online account
