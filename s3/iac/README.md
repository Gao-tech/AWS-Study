# [CDK GIT](https://github.com/aws/aws-cdk)

## Getting Started

For a detailed walkthrough, see the [tutorial](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#hello_world_tutorial) in the AWS CDK [Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/home.html).

### At a glance

Install or update the [AWS CDK CLI] from npm (requires [Node.js ≥ 14.15.0](https://nodejs.org/download/release/latest-v14.x/)). We recommend using a version in [Active LTS](https://nodejs.org/en/about/previous-releases)

```sh
npm i -g aws-cdk
```

(See [Manual Installation](./MANUAL_INSTALLATION.md) for installing the CDK from a signed .zip file).

Initialize a project:

```sh
mkdir hello-cdk
cd hello-cdk
cdk init sample-app --language=typescript
```

This creates a sample project looking like this:

```ts
export class HelloCdkStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const queue = new sqs.Queue(this, "HelloCdkQueue", {
      visibilityTimeout: cdk.Duration.seconds(300),
    });

    const topic = new sns.Topic(this, "HelloCdkTopic");

    topic.addSubscription(new subs.SqsSubscription(queue));
  }
}
```

Deploy this to your account:

```sh
cdk deploy
```

Use the `cdk` command-line toolkit to interact with your project:

- `cdk deploy`: deploys your app into an AWS account
- `cdk synth`: synthesizes an AWS CloudFormation template for your app
- `cdk diff`: compares your app with the deployed stack
