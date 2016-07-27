# Contacts Application

#### Synopsis
- A simple contacts application supporting `add contact` and `search contact` functions. 
- Search is prefix-based and case in-sensitive. 
- Using prefix tree ([trie](https://en.wikipedia.org/wiki/Trie)) to store the contacts.

#### Running App and Tests
1. To run the app: 
    `python -m src.contacts`
2. To run the tests: 
    `make test`

#### Example
```
1) Add contact 2) Search 3) Exit
1
Enter name: Sachin Kale
1) Add contact 2) Search 3) Exit
1
Enter name: Kale Subhash
1) Add contact 2) Search 3) Exit
1
Enter name: Satish Sinha
1) Add contact 2) Search 3) Exit
1
Enter name: Sachin
1) Add contact 2) Search 3) Exit
2
Enter name: Kale
Sachin Kale
Kale Subhash
1) Add contact 2) Search 3) Exit
2
Enter name: Sachin
Sachin
Sachin Kale
1) Add contact 2) Search 3) Exit
2
Enter name: S
Sachin
Sachin Kale
Satish Sinha
Kale Subhash
1) Add contact 2) Search 3) Exit
2
Enter name: Xyz
1) Add contact 2) Search 3) Exit
3
Happy Searching
```
