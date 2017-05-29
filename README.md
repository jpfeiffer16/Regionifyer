# Regionifyer
A little program that maps ip addresses to AWS regions

## Usage

`$ git clone <git ssh enpoint>`

`$ cd regionifyer`

`$ ./regionifyer.py <valid IPv4 address>`

```
us-west-2
```

## Implementation Details
* Gets JSON from https://ip-ranges.amazonaws.com/ip-ranges.json
* Runs through the ip list and sees if there is a direct match for ip.
  * If there is then it uses that ip
* If there is no direct ip match, it trys to match the 1st, and 2nd octets.
  * If it cannot match this, fail.
* If it can match that, it then finds out the two mappings with the 3rd octet greater and less than the 3rd octet of the given ip
* Print out that it could be either of those mappings.