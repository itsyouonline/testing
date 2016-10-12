##Test Case 1: POST user 

**Purpose: Test add user using post /users is working as expected**

**Steps:**

1. add user, should succeed
2. validate that the user is added as expected


##Test Case 1: POST user emailaddresses

**Purpose: Test add user emailaddresses using post /users/{username}/emailaddresses is working as expected**

**Steps:**

1. add user emailaddress, should succeed
2. validate that the user emailaddress is added as expected


##Test Case 1: POST user emailaddresses validate

**Purpose: Test add user emailaddresses validate using post /users/{username}/emailaddresses/{label}/validate is working as expected**

**Steps:**

1. validate user emailaddress, should succeed
2. validate that the user emailaddress is validated as expected


##Test Case 1: POST user emailaddresses

**Purpose: Test add user emailaddresses using post /users/{username}/apikeys is working as expected**

**Steps:**

1. add user emailaddress, should succeed
2. validate that the user emailaddress is added as expected


##Test Case 1: POST user registry

**Purpose: Test add user registry using post /users/{username}/registry is working as expected**

**Steps:**

1. add user registry, should succeed
2. validate that the user registry is added as expected


##Test Case 1: POST user emailaddrtotpesses

**Purpose: Test add user totp using post /users/{username}/totp is working as expected**

**Steps:**

1. add user totp, should succeed
2. validate that the user totp is added as expected


##Test Case 1: POST user addresses

**Purpose: Test add user addresses using post /users/{username}/addresses is working as expected**

**Steps:**

1. add user addresses, should succeed
2. validate that the user addresses is added as expected


##Test Case 1: POST user digitalwallet

**Purpose: Test add user digitalwallet using post /users/{username}/digitalwallet is working as expected**

**Steps:**

1. add user digitalwallet, should succeed
2. validate that the user digitalwallet is added as expected


##Test Case 1: POST user phonenumbers

**Purpose: Test add user phonenumbers using post /users/{username}/phonenumbers is working as expected**

**Steps:**

1. add user phonenumber, should succeed
2. validate that the user phonenumber is added as expected


##Test Case 1: POST user phonenumbers activate

**Purpose: Test add user phonenumbers activate using post /users/{username}/phonenumbers/{label}/activate is working as expected**

**Steps:**

1. activate user emailaddress, should succeed
2. validate that the user emailaddress is activated as expected


##Test Case 1: POST user contracts

**Purpose: Test add user contracts using post /users/{username}/contracts is working as expected**

**Steps:**

1. add user contract, should succeed
2. validate that the user contract is added as expected


##Test Case 1: POST user organizations roles

**Purpose: Test add user organizations roles using post /users/{username}/organizations/{globalid}/roles/{role} is working as expected**

**Steps:**

1. add user organizations role, should succeed
2. validate that the user organizations role is added as expected



/organizations
/organizations/{globalid}
/organizations/{globalid}/owners
/organizations/{globalid}/contracts
/organizations/{globalid}/apikeys
/organizations/{globalid}/registry
/organizations/{globalid}/dns

/companies
/companies/{globalId}
/companies/{globalId}/contracts

/contracts/{contractId}/signatures

