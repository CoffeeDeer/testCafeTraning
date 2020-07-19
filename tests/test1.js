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
