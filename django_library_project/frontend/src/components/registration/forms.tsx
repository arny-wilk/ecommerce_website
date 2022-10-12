import React from "react";
import {
  Formik,
  FormikHelpers,
  FormikProps,
  Form,
  Field,
  FieldProps,
} from "formik";

interface MyFormValues {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  password: string;
}

export const MyApp: React.FC<{}> = () => {
  const initialValues: MyFormValues = {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
    password: ""
  };
  return (
    <div>
      <h1>Sign up form</h1>
      <Formik
        initialValues={initialValues}
        onSubmit={(values, actions) => {
          console.log({ values, actions });
          alert(JSON.stringify(values, null, 2));
          actions.setSubmitting(false);
        }}
      >
        <Form>
          <label htmlFor="firstName">First Name</label>
          <Field id="firstName" type="text" name="firstName" placeholder="Your First Name" />
          <label htmlFor="lastName">Last Name</label>
          <Field id="lastName" type="text" name="lastName" placeholder="Your Last Name" />
          <label htmlFor="email">email</label>
          <Field id="email" type="email" name="email" placeholder="your email" />
          <label htmlFor="phone">phone</label>
          <Field id="phone" type="phone" name="phone" placeholder="your phone" />
          <label htmlFor="password">password</label>
          <Field id="password" type="password" name="password" placeholder="Your password here" />
          <button type="submit">Submit</button>
        </Form>
      </Formik>
    </div>
  );
};
