import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Todo Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="todo-title">Title</Label>
              <Input
                type="text"
                id="todo-title"
                name="name"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter dog's name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-breed">Breed</Label>
              <Input
                type="text"
                id="todo-breed"
                name="breed"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter dog's breed"
              />
            </FormGroup>
            <FormGroup>
              <Label for="todo-age">Age</Label>
              <Input
                type="text"
                id="todo-age"
                name="age"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter dog's age"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
