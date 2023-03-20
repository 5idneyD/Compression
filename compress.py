# Import sys module to read which text file is being parsed to code
import sys

# Function used to compress
def compress(text):
    # convert file string to list so we can replace chars
    text = list(text)
    # find length of all chars to loop through
    length = len(text)
    a = []
    
    # Loop through document and replace all consecutive chars with "`"
    # The new text string is then saved in to a new list
    for i in range(length):
        try:
            if text[i] == text[i-1]:
                a.append("`")
            else:
                a.append(text[i])
        except IndexError:
            pass
        
    # Loop through next document that contains "`" in place of consecutive char, and record number of consecutive "`"s
    # Add record to list
    # replace each "`" with the number of consecutive "`"s, and increase te count by 1
    # If the next char is not "`", reset the count to 1
    counts = []
    count = 1
    for i in a:
        if i != "`":
            count = 1
        else:
            count += 1
        # print(i, count)
        counts.append(count)

    # Loop through text and number of consecutive "`"
    # replace consecutive "`" with the count number
    for i, j, k in zip(a, counts, range(len(a))):
        if j == 1:
            pass
        else:
            a[k] = str(j)
    
    # Remove consecutive numbers representing consecutive "`", so only the original char and the count remain
    result = []
    for i in range(len(a)):
        try:
            if int(a[i+1]) == int(a[i]) + 1:
                pass
            else:
                result.append(a[i])
        except IndexError:
            result.append(a[i])
        except ValueError:
            result.append(a[i])
            
    # Combine final list to string and return
    text = "".join(result)
    return text.encode()

with open(sys.argv[1], "r") as f:
    text = f.read()
    result = compress(text)
    file_name = sys.argv[1].replace(".txt", "")

with open(file_name + " - compressed.txt", "wb") as h:
        h.write(result)