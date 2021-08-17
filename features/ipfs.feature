Feature: showing off behave

  Scenario: IPFS file added with index option should be indexed
    Given we have IPFS node installed
    Given we have TimeRose deployed
    When we add a test file to IPFS
    Then we can find provider from TimeRose