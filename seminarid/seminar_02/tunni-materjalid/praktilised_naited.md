# Reacti koodinäidis erinevate case-ide kasutamiseks

## Selgitused:
PascalCase – kasutatakse Reacti komponentide nimedes (MyComponent, ProfileHeader).  

camelCase – kasutatakse muutujate ja funktsioonide nimedes (userName, handleButtonClick).  

snake_case – kasutatakse konstantselt või andmete nimedes, nagu user_profile_image_url.  

kebab-case – kasutatakse CSS klassinimedes, nagu .profile-header, .btn-primary.

## Näide:
```jsx
// PascalCase – kasutatakse komponendi nimedes
import React from 'react';

// PascalCase komponent
function MyComponent() {
  // camelCase – kasutatakse muutujate ja funktsioonide nimedes
  const userName = 'John Doe';

  // snake_case – kasutatakse tavaliselt andmebaasides või konstantide puhul
  const user_profile_image_url = 'https://example.com/johndoe.jpg';

  // Funktsioon, mis kasutab camelCase-i
  function handleButtonClick() {
    console.log('Nuppu vajutati!');
  }

  return (
    <div className="container">
      {/* PascalCase komponentide kasutamine */}
      <ProfileHeader userName={userName} userProfileImage={user_profile_image_url} />
      <button onClick={handleButtonClick} className="btn btn-primary">
        Click Me
      </button>
    </div>
  );
}

// PascalCase – teine komponent
function ProfileHeader({ userName, userProfileImage }) {
  return (
    <div className="profile-header">
      <img src={userProfileImage} alt={userName} className="profile-image" />
      <h1 className="profile-name">{userName}</h1>
    </div>
  );
}

export default MyComponent;
```
CSS-i näide:
```css
/* CSS näidis – kebab-case kasutatakse klassinimedes */
.container {
  max-width: 1200px;
  margin: 0 auto;
}

.profile-header {
  display: flex;
  align-items: center;
  padding: 20px;
}

.profile-image {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}

.profile-name {
  margin-left: 10px;
  font-size: 24px;
  font-weight: bold;
}

.btn-primary {
  background-color: #007bff;
  border: none;
  padding: 10px 20px;
  color: white;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}
```

