# Visual Attribution
## Task
Visual attribution is the problem of identifying object features using its photo.
This problem is very important as it is often used as part of a solution for a wide range of tasks. 
Among these tasks can be:

* Making a well-attributed catalog which will give users the ability to filter product specifying their characteristics.
* Making recommendations showing similar products.
* Making visual search allowing to find products by images.

In this showcase, we will show what is a visual attribution solving this problem for women dresses. 
At the end of the path, you could upload an image with a dress and get a prediction for such attributes as length and color.
## Data
To train the model you need data. You can use this
[data](https://storage.googleapis.com/dell-ml-datasets/visual-attribution/data.tar.gz)
which holds on Google Cloud Storage and is publicly available.

<table>
  <tr>
    <td><img src='assets/testdata/test-1.jpg' width="200" height="200"/></td>
    <td><img src='assets/testdata/test-2.jpg' width="200" height="200"/></td>
    <td><img src='assets/testdata/test-3.jpg' width="200" height="200"/></td>
    <td><img src='assets/testdata/test-4.jpg' width="200" height="200"/></td>
  </tr>
</table>


## Environment
AWS
* SageMaker
* S3 buckets to store data
* ECS to deploy backend service with UI

<img src='assets/aws-design.png' width="600" height="455"/>

## Backend-UI

<img src='assets/animation.gif' width="900" height="600"/>