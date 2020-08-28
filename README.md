# stockscraper
Python script that scrapes selected stocks into a SQLite database

### Setup
##### Dependencies
`pip install requests`

##### Running
Create an auth.json file in the root directory with your IEXCloud tokens such as
```
{
    "testToken": "your-test-token-here",
    "realToken": "your-real-token-here",
    "mode": "(test or real)"
}
```
Choose the test mode to use the sandbox IEXcloud data for testing and real for actual data storage.
