import validador from 'validator'

class FormValidator{

    constructor(validations){
        this.validations = validations
    }

    validate(state){
        let validation = this.valid()
        
        this.validations.forEach(rule => {
            
            const field = state[rule.field.toString()]
            const validationMethod = validador[rule.method]

            if(validationMethod(field, [], state)){
                validation[rule.field] = {
                    isInvalid: true,
                    message: rule.message,
                    name:rule.field
                }
                validation.isValid = false
            }
        });
        return validation;
    }

    valid(){
        const validation = {}
    
        this.validations.map(rule => (
            validation[rule.field] = {isInvalid: false, message: '', name:rule.field}
        ));
    
        return {isValid: true, ...validation};
    } 
}

export default FormValidator;