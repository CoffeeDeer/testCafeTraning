import { Selector } from "testcafe";

fixture`Getting Started`.page`http://devexpress.github.io/testcafe/example`;

test("My first test", async (t) => {
    //debugger;
    await t
        .typeText("#developer-name", "John Smith")
        .click("#submit-button")
        //change page
        .expect(Selector("#article-header").innerText)
        .eql("Thank you, John Smith!");

    const articleHeader = await Selector(".result-content").find("h1");

    // Obtain the text of the article header
    let headerText = await articleHeader.innerText;
});

fixture`My fixture`;

test("Test1", async (t) => {
    /* Test 1 Code */
});

test("Test2", async (t) => {
    /* Test 2 Code */
});

fixture`MyFixture2`
    .meta("fixtureID", "f-0001")
    .meta({ author: "John", creationDate: "05/03/2018" });

test.page`http://devexpress.github.io/testcafe/example`("MyTest", async (t) => {
    /* ... */
});

//specificPage
test
    .meta("testID", "t-0005")
    .meta({ severity: "critical", testedAPIVersion: "1.0" })
    .page`http://devexpress.github.io/testcafe/blog/`(
    "specificPage test",
    async (t) => {
        // Starts at http://devexpress.github.io/testcafe/blog/
    }
);

fixture`My fixture`
    .page`http://example.com`
    .beforeEach(async (t) => {
        await t.useRole(admin).click("#open-management-console");
    })
    .afterEach(async (t) => {
        await t.click("#delete-data");
    });

test.before(async (t) => {
    await t.useRole(admin).click("#open-management-console");
})("MyTest", async (t) => {
    /* ... */
}).after(async (t) => {
    await t.click("#delete-data");
});


fixture.skip `Fixture 1`; // All tests in this fixture are skipped

test('Fixture 1 - Test 1', () => {});
test('Fixture 1 - Test 2', () => {});

fixture `Fixture 2`;

test('Fixture 2 - Test 1', () => {});
test.skip('Fixture 2 - Test 2', () => {}); // This test is skipped
test('Fixture 2 - Test 3', () => {});